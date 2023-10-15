"""
This is the main entry for Engine. 
"""
from Logging.logging_config import logger
from Simulator.simulate_main import simulate_main


logger.info("Starting Engine...")
simulate_main()
logger.info("Exiting Engine...")
