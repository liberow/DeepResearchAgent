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
from src.models import model_manager
from src.agent import create_agent
from src.utils import assemble_project_path

async def main():
    # Init logger
    config.init_config(config_path=assemble_project_path("configs/config_liber.toml"))
    log_path = config.log_path
    logger.init_logger(log_path)
    logger.info(f"Initializing logger: {log_path}")
    logger.info(f"root path: {root}")

    # Registed models
    model_manager.init_models(use_local_proxy=config.use_local_proxy)
    logger.info("Registed models: %s", ", ".join(model_manager.registed_models.keys()))
    
    # Create agent
    agent = create_agent()

    # Run example
    task = "广东省具身智能产业链分析"
    res = await agent.run(task)
    logger.info(f"Result: {res}")

if __name__ == '__main__':
    asyncio.run(main())