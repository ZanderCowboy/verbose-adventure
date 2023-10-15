"""
This is the main entry for Engine. 
"""
from engine_logging.logging_config import logger
from simulator.simulate_main import simulate_main


logger.info("Starting Engine...")
simulate_main()
logger.info("Exiting Engine...")
