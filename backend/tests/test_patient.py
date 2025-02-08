import pytest
from httpx import AsyncClient
from backend.api.schemas.patient import PatientCreate


@pytest.mark.asyncio
async def test_create_patient(client: AsyncClient):
    patient_data = {
        "first_name": "Петр",
        "last_name": "Петров",
        "middle_name": "Петрович",
        "username": "patient_petr",
        "password": "secret",
        "insurance": "123456789"
    }
    response = await client.post('/patient/', json=patient_data)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['username'] == patient_data['username']
