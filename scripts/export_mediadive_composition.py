#!/usr/bin/env python3
"""
Export MediaDive composition data from MongoDB.

This script connects to the local MongoDB database and exports:
- medium_composition: Medium-to-ingredient relationships
- medium_strains: Medium-to-organism relationships
"""

import json
from pathlib import Path
from pymongo import MongoClient

# MongoDB connection
MONGODB_URI = "mongodb://localhost:27017"
DATABASE_NAME = "mediadive"

# Output directory
OUTPUT_DIR = Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/raw/mediadive")


def export_collection(db, collection_name: str, output_file: Path):
    """Export a MongoDB collection to JSON."""
    collection = db[collection_name]

    # Get all documents
    documents = list(collection.find({}))

    # Convert ObjectId to string
    for doc in documents:
        if '_id' in doc:
            doc['_id'] = str(doc['_id'])

    # Write to file
    with open(output_file, 'w') as f:
        json.dump(documents, f, indent=2)

    print(f"✓ Exported {len(documents)} documents from {collection_name} to {output_file}")
    return len(documents)


def main():
    """Export composition and strain data from MongoDB."""
    print("=" * 60)
    print("MediaDive Composition Data Export")
    print("=" * 60)

    try:
        # Connect to MongoDB
        print(f"\nConnecting to MongoDB at {MONGODB_URI}...")
        client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

        # Test connection
        client.server_info()
        print("✓ Connected to MongoDB")

        # Get database
        db = client[DATABASE_NAME]

        # Create output directory
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Export medium_composition
        print("\n1. Exporting medium_composition...")
        comp_count = export_collection(
            db,
            "medium_composition",
            OUTPUT_DIR / "medium_composition_data.json"
        )

        # Export medium_strains
        print("\n2. Exporting medium_strains...")
        strain_count = export_collection(
            db,
            "medium_strains",
            OUTPUT_DIR / "medium_strains_data.json"
        )

        # Create summary
        summary = {
            "export_date": "2025-01-24",
            "composition_records": comp_count,
            "strain_records": strain_count,
            "database": DATABASE_NAME,
            "collections": ["medium_composition", "medium_strains"]
        }

        with open(OUTPUT_DIR / "composition_export_stats.json", 'w') as f:
            json.dump(summary, f, indent=2)

        print("\n" + "=" * 60)
        print("✓ Export complete!")
        print(f"  Composition records: {comp_count}")
        print(f"  Strain records: {strain_count}")
        print(f"  Output directory: {OUTPUT_DIR}")
        print("=" * 60)

        # Close connection
        client.close()

    except Exception as e:
        print(f"\n✗ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Check if MongoDB is running: brew services list")
        print("2. Start MongoDB: brew services start mongodb-community")
        print("3. Wait ~10 seconds for MongoDB to fully start")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
