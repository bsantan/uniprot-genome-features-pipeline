import click
from uniprot_utils import run_api

@click.group()
def main():
    """CLI."""
    pass


@main.command("download-uniprot-genomes")
@click.option("api", "-a", required=True, default="uniprot", multiple=False)
@show_status_option
def get_data_via_api(api: str, show_status: bool) -> None:
    """
    Get data via rest API.

    :param api: A string pointing to the API to upload data to.
    :return: None
    """

    run_api(api, show_status)

if __name__ == "__main__":
    main()