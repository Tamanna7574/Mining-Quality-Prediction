from pydantic import BaseModel


class MiningInput(BaseModel):

    # Example

    Iron_Feed: float
    Silica_Feed: float
    Starch_Flow: float
    Amina_Flow: float
    Ore_Pulp_Flow: float
    Ore_Pulp_pH: float
    Ore_Pulp_Density: float