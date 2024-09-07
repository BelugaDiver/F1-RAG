from typing import Optional, Type

from langchain_community.tools import BaseSQLDatabaseTool
from langchain_core.callbacks import (CallbackManagerForToolRun)
from langchain_core.tools import BaseTool
from langchain.pydantic_v1 import BaseModel, Field

class DBSchemaToolInput(BaseModel):
    table_name: str = Field(description="Table to retrieve db schema for.")

class ViewAndTableDBSchemaTool(BaseSQLDatabaseTool, BaseTool):
    """Tool that provides information about database tables and views."""

    name: str = "db_schema_tool"
    description: str = "provides schema information about database tables or views"
    args_schema: Type[BaseModel] = DBSchemaToolInput

    def _run(self, table_name: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool to fetch schemas for database objects, including tables or views."""

        schema = self.config.db.run_no_throw(command=f"PRAGMA table_xinfo({table_name})", fetch="all", include_columns=True)
        return schema
