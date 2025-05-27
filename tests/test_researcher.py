import warnings
warnings.simplefilter("ignore", DeprecationWarning)

import sys
from pathlib import Path
import asyncio

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)

from src.models import model_manager
from src.tools.deep_researcher import DeepResearcherTool

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(verbose=True)
    
    model_manager.init_models(use_local_proxy=False)
    
    model = model_manager.registed_models['gpt-4.1']

    task = """
    Under DDC 633 on Bielefeld University Library's BASE, as of 2020, from what country was the unknown language article with a flag unique from the others? 
    """

    deep_research = DeepResearcherTool(model=model)
    results = asyncio.run(deep_research.forward(task))
    print(results)