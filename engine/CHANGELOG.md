# Changes in code

## V0.0.7
- Created a new Logging package to contain all logging related code. 
- Created logging_config using Python logging, printing logs to console and files
- Created log folder and files as Output/engine.log, Output/engine.log.1, etc.
- Created a rotator for log files, so that a log history can be kept.
- Added logging throughout the code.
- Finished some documentation. 
- Refactored code, removing redundant parts. 
- Added more TODOs for later development.
- Created a new generalized printing function in PrintDetails.py used to do 
'sections of output' logging

## v0.0.6
- Created a constants file containing all the constants that is used in the code
- Created a new file CreateElements.py, moving the array creation to it and out
  of CreateConditionals.py
- Did code refactoring and restructuring
- Worked on the DisplayMatrix.py file for the output of the T/F matrix to console
- Cleaned up the PropositionalRules.py
- Created CheckBrackets.py, to be used as one of the checks for incoming statements
- Created CheckForIllegalCharacters.py that checks for illegal characters as above
- Cleaned up AnalyzeFunction.py
- Cleanup up and refactored ParseFunction.py
- Created SimulateMain.py that can be used as main instead of Main.py
- Cleaned up UserInput.py
- Restructured files into Parser/Validate since the Validation package was empty
- Deleted DumpFile.py and LogicCalculator.py

## v0.0.5
- created packages: Components, Computation, GRPCServer, Parser, Simulator, Validation
- refactored exiting code and moved it around
- IN PROGRESS: added metadata to existing code
- tested a try-catch block with Parser.Checks
- created Simulator.SimulateServer.py to simulate the input and responses generated 
    from using the GRPCServer
- Moved existing code into single files, following the SOLID principle

## v0.0.2 - v0.0.4
- Added small changes over time. 

## v0.0.1
- needs restructuring

## v0.0.0
- initial code copied from other project