# ElementSim

A FastAPI microservice simulating medieval chemistry and crafting with scientific accuracy. Combines elements through thermal, chemical, and mechanical processes based on historical understanding. Features realistic element interactions, recipe discovery, and skill-based crafting success rates.

## Overview

ElementSim models the chemical and crafting processes of the medieval era (roughly 5th-15th century), focusing on:

- **Alchemy & Early Chemistry**: Medieval understanding of material properties and transformations
- **Metallurgy**: Smelting ores, creating alloys, and working with metals
- **Herbalism**: Processing plants for medicinal, practical, and alchemical uses
- **Brewing & Fermentation**: Creating alcohols and other fermented products

The simulation aims to be historically authentic while still providing an engaging and accessible system.

## Features

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
│   ├── data/                    # Seed data
│   └── utils/                   # Utility functions
├── tests/                       # Test suite
├── alembic/                     # DB migrations
└── scripts/                     # Utility scripts
```

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL (optional, SQLite for development)
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ElementSim.git
   cd ElementSim
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   # Using SQLite (development)
   alembic upgrade head

   # Or with PostgreSQL
   # Update DATABASE_URL in .env file
   # Then run: alembic upgrade head
   ```

5. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at http://localhost:8000, with interactive documentation at http://localhost:8000/docs.

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

## API Examples

### Crafting an Item

```bash
curl -X POST "http://localhost:8000/api/v1/craft" \
  -H "Content-Type: application/json" \
  -d '{
    "recipe_id": 1,
    "inventory": {"1": 2.0, "3": 1.5},
    "skill_level": 3
  }'
```

### Exploring Element Interactions

```bash
curl -X POST "http://localhost:8000/api/v1/simulate/interaction" \
  -H "Content-Type: application/json" \
  -d '{
    "element1_id": 2,
    "element2_id": 5
  }'
```

## Future Plans

- **LLM Integration**: Enhanced descriptions and dynamic recipe generation
- **MCP Server**: Exposing as a microservice for other applications
- **Advanced Visualization**: Visual representation of reactions and processes
- **Historical Timeline**: Element and process discovery based on historical periods

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).