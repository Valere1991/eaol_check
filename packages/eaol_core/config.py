from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    env: str = "local"
    ai_provider: str = "mock"
    openai_api_key: str | None = None
    postgres_dsn: str = "postgresql://eaol:eaol@localhost:5432/eaol"
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "eaol-local-password"
    zeebe_address: str = "localhost:26500"
    default_tenant_id: str = "demo"

    model_config = SettingsConfigDict(env_prefix="EAOL_", env_file=".env", extra="ignore")


settings = Settings()
