import json
import pytest

from httpx import AsyncClient

from main import app

@pytest.mark.anyio
async def test_folder_create():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/folder/", content=json.dumps(
                {
                    "user_team_id": 1,
                    "user_id": 1,
                    "team_id": 1,
                    "divider": True
                }
            ),
        )

        assert response.status_code == 201
        assert response.json() == {
            "message": None,
            "data": {
                "id": response.json()["data"]["id"],
                "user_team_id": 1,
                "user_id": 1,
                "team_id": 1,
                "divider": True
            }
        }