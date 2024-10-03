from config import DatabaseSettings

database_settings = DatabaseSettings(_env_file='.env.dev')


def test_main():
    # Given
    expected_pg_host = 'dev_pghost'
    # When
    actual_pg_host = database_settings.PG_HOST
    # Then
    assert actual_pg_host == expected_pg_host
