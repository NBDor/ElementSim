# ElementSim

A FastAPI microservice simulating medieval chemistry and crafting with scientific accuracy. Combines elements through thermal, chemical, and mechanical processes based on historical understanding.

## Overview

ElementSim models the chemical and crafting processes of the medieval era (roughly 5th-15th century), focusing on:

- **Alchemy & Early Chemistry**: Medieval understanding of material properties and transformations
- **Metallurgy**: Smelting ores, creating alloys, and working with metals
- **Herbalism**: Processing plants for medicinal, practical, and alchemical uses
- **Brewing & Fermentation**: Creating alcohols and other fermented products

The simulation aims to be historically authentic while still providing an engaging and accessible system.

## Project Status

This project is currently in early development. The basic infrastructure is set up, but most features are not yet implemented.

### Current Status
- ✅ Basic project structure established
- ✅ Database models defined
- ✅ Docker configuration complete
- ✅ Alembic migrations set up
- ⬜ API endpoints (in progress)
- ⬜ Element interaction simulation (planned)
- ⬜ Crafting mechanics (planned)
- ⬜ Recipe discovery (planned)

## Features (Planned)

- **Element System**: Diverse materials with realistic properties and medieval classifications
- **Process Simulation**: Thermal, chemical, and mechanical transformation processes
- **Recipe Discovery**: Find and learn new combinations through experimentation
- **Skill Progression**: Improve success rates and output quality with practice
- **Scientifically Grounded**: Based on actual medieval understanding of materials
- **RESTful API**: Easy integration with various frontend applications

## Project Structure

```
ElementSim/
├── app/
│   ├── api/                     # API endpoints
│   ├── core/                    # Core configuration
│   ├── db/                      # Database utilities
│   ├── models/                  # SQLAlchemy models
│   ├── schemas/                 # Pydantic schemas
│   ├── services/                # Business logic
│   └── utils/                   # Utility functions
├── tests/                       # Test suite
├── alembic/                     # DB migrations
└── scripts/                     # Utility scripts
```

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Docker and Docker Compose (for containerized deployment)

### Running with Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ElementSim.git
   cd ElementSim
   ```

2. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

The API will be available at http://localhost:8000

### Local Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ElementSim.git
   cd ElementSim
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables (create a .env file):
   ```
   POSTGRES_SERVER=localhost
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=element_sim
   POSTGRES_PORT=5432
   SECRET_KEY=your_secret_key_here
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Core Concepts

### Elements

Elements are the basic materials in the simulation, classified according to medieval understanding:

- **Four Elements Theory**: Earth, Air, Fire, Water
- **Properties**: Hot/Cold, Wet/Dry
- **Categories**: Metals, Minerals, Herbs, Liquids, Organic materials

### Processes

Transformative methods used to create new substances:

- **Thermal**: Smelting, Melting, Calcination
- **Chemical**: Fermentation, Distillation, Dissolution
- **Mechanical**: Grinding, Mixing, Pounding
- **Specialized**: Alchemical procedures, Transmutation attempts

### Recipes

Defined combinations of elements, processes, and conditions that produce reliable outcomes.

## Future Plans

- **Full API Implementation**: Complete all planned endpoints
- **Element Interaction Engine**: Realistic simulation of chemical interactions
- **Recipe Discovery System**: Dynamic discovery of new combinations
- **LLM Integration**: Enhanced descriptions and dynamic recipe generation
- **Advanced Visualization**: Visual representation of reactions and processes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.