# SHELL		:=	/bin/bash

DEFAULT		=	\033[0m
RED			=	\033[1;31m
CYAN		=	\033[1;36m
PINK		=	\033[1;35m
GREEN		=	\033[1;32m
YELLOW		=	\033[1;33m
REWHITE		=	\033[1;7;97m
RECYAN		=	\033[1;7;36m
REPINK		=	\033[1;7;35m
RERED		=	\033[1;7;31m
REGREEN		=	\033[1;7;32m
REYELLOW	=	\033[1;7;33m

how:
	@clear
	@echo "$(PINK)To create virtual environment, run: $(YELLOW)python3 -m venv venv$(DEFAULT)"
	@echo "$(PINK)Then run: $(YELLOW)source venv/bin/activate $(PINK)to activate the venv$(DEFAULT)"
	@echo "$(PINK)Run: $(YELLOW)pip install -r requirements.txt $(PINK) or $(YELLOW) pip install -r requirements.txt --break-system-packages$(PINK) to install all requirements$(DEFAULT)"
	@echo "$(PINK)Run: $(YELLOW)docker-compose up -d $(PINK)to create the database$(DEFAULT)"
	@echo "$(PINK)Run: $(YELLOW)python3 -c 'from src.contrib.database import Base, engine; Base.metadata.create_all(bind=engine)' $(PINK)to migrate datas$(DEFAULT)"
	@echo "$(PINK)Run: $(YELLOW)make run $(PINK)to run the API$(DEFAULT)"
	@echo "$(PINK)Run: $(YELLOW)deactivate $(PINK)to deactivate the venv$(DEFAULT)"

run:
	@uvicorn src.main:app --reload

see_map:
	@clear
	@cat ../file_map

clean:
	@rm -rfd venv
	@echo "$(GREEN) virtual environment were deleted successfully! $(DEFAULT)"