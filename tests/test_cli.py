"""CLI tests."""
from tests.helpers import ProjectMock


def test_simple_error(request):
    """A simple error on the CLI."""
    project = (
        ProjectMock(request)
        .style(
            """
        ["pyproject.toml".tool.black]
        line-length = 100
        """
        )
        .pyproject_toml(
            """
        [tool.blabla]
        something = 22
        """
        )
    )

    project.assert_cli_output(
        f"""
        {str(project.root_dir)}/pyproject.toml:1: NIP318  has missing values:
        [tool.black]
        line-length = 100
        """
    )