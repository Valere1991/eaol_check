from fastapi import APIRouter, HTTPException

from packages.eaol_core.sectors.catalog import SECTOR_PACKS, SectorPack

router = APIRouter(prefix="/api/v1/sectors", tags=["sectors"])


@router.get("", response_model=list[SectorPack])
def list_sector_packs() -> list[SectorPack]:
    return list(SECTOR_PACKS.values())


@router.get("/{sector_key}", response_model=SectorPack)
def get_sector_pack(sector_key: str) -> SectorPack:
    sector = SECTOR_PACKS.get(sector_key)
    if sector is None:
        raise HTTPException(status_code=404, detail="Unknown sector pack")
    return sector
