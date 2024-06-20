"""Entrypoint."""

import argparse
from migration_manager import MigrationManager


def main():
    """Entrypoint"""
    migration_manager = MigrationManager()
    parser = argparse.ArgumentParser(description="Migrate or delete repositories.")
    parser.add_argument(
        "action",
        choices=["import", "delete"],
        help="The action to perform: import or delete repositories.",
    )

    args = parser.parse_args()

    if args.action == "import":
        migration_manager.migrate_all_repos()
    elif args.action == "delete":
        migration_manager.delete_all_repos_migrated()


if __name__ == "__main__":
    main()
