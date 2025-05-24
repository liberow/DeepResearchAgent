import warnings
warnings.simplefilter("ignore", DeprecationWarning)
from src.utils import assemble_project_path

import sys
from pathlib import Path
import asyncio

root = str(Path(__file__).resolve().parents[4])
sys.path.append(root)

from src.logger import logger
from src.config import config
from src.registry import REGISTED_MODELS
from src.agent import create_agent

async def main():
    # Init logger
    config.init_config(config_path=assemble_project_path("configs/config_liber.toml"))
    log_path = config.log_path
    logger.init_logger(log_path)
    logger.info(f"Initializing logger: {log_path}")
    logger.info(f"root path: {root}")

    # Registed models
    logger.info("Registed models: %s", ", ".join(REGISTED_MODELS.keys()))
    
    # Create agent
    agent = create_agent()

    # Run example
    task = "Search for the latest research paper on the topic of 'AI Agent' and summarize it."
    res = await agent.run(task)
    logger.info(f"Result: {res}")

if __name__ == '__main__':
    asyncio.run(main())