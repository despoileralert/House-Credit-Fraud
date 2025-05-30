#!/usr/bin/env python3
"""
MLOps Classification Project Structure Creator
Creates the complete directory structure and empty files for the MLOps project.
"""

import os
from pathlib import Path

def create_mlops_project_structure(project_name="House-Credit-Fraud"):
    """
    Creates the complete MLOps project directory structure with empty files.
    
    Args:
        project_name (str): Name of the project directory
    """
    
    # Define the project structure
    structure = {
        # Root files
        "": [
            "README.md",
            "requirements.txt", 
            "setup.py",
            ".env.example",
            ".gitignore",
            ".dvcignore",
            "dvc.yaml",
            "params.yaml",
            "mlproject",
            "docker-compose.yml",
            "Dockerfile"
        ],
        
        # Config directory
        "config": [
            "__init__.py",
            "app_config.yaml",
            "database_config.yaml", 
            "spark_config.yaml",
            "mlflow_config.yaml",
            "evidently_config.yaml"
        ],
        
        # Source code structure
        "src": ["__init__.py"],
        
        # Entities
        "src/entities": [
            "__init__.py",
            "base_entity.py",
            "dataset_entity.py",
            "feature_entity.py",
            "model_entity.py",
            "experiment_entity.py",
            "prediction_entity.py",
            "report_entity.py",
            "pipeline_entity.py"
        ],
        
        # Repositories
        "src/repositories": [
            "__init__.py",
            "base_repository.py",
            "mysql_repository.py",
            "mlflow_repository.py",
            "feature_repository.py",
            "dvc_repository.py",
            "evidently_repository.py"
        ],
        
        # Services
        "src/services": [
            "__init__.py",
            "data_service.py",
            "feature_service.py",
            "training_service.py",
            "inference_service.py",
            "evaluation_service.py",
            "monitoring_service.py",
            "pipeline_service.py"
        ],
        
        # Factories
        "src/factories": [
            "__init__.py",
            "spark_factory.py",
            "model_factory.py",
            "feature_factory.py",
            "repository_factory.py",
            "service_factory.py"
        ],
        
        # Processors
        "src/processors": [
            "__init__.py",
            "data_processor.py",
            "feature_processor.py",
            "model_processor.py",
            "report_processor.py"
        ],
        
        # Utils
        "src/utils": [
            "__init__.py",
            "config_manager.py",
            "logger.py",
            "validator.py",
            "exceptions.py",
            "decorators.py"
        ],
        
        # Tests structure
        "tests": [
            "__init__.py",
            "conftest.py"
        ],
        
        "tests/unit": ["__init__.py"],
        "tests/unit/entities": ["__init__.py"],
        "tests/unit/repositories": ["__init__.py"],
        "tests/unit/services": ["__init__.py"],
        "tests/unit/processors": ["__init__.py"],
        
        "tests/integration": [
            "__init__.py",
            "test_database_integration.py",
            "test_mlflow_integration.py",
            "test_pipeline_integration.py"
        ],
        
        "tests/fixtures": ["__init__.py"],
        "tests/fixtures/sample_datasets": [],
        "tests/fixtures/mock_configs": [],
        
        # Notebooks
        "notebooks": [
            "01_data_exploration.ipynb",
            "02_feature_analysis.ipynb",
            "03_model_experimentation.ipynb",
            "04_monitoring_analysis.ipynb"
        ],
        
        # Data directories (DVC tracked)
        "data": [],
        "data/raw": [],
        "data/processed": [],
        "data/features": [],
        "data/predictions": [],
        
        # Models directory (DVC tracked)
        "models": [],
        "models/experiments": [],
        "models/production": [],
        "models/staging": [],
        
        # Reports directory (DVC tracked)
        "reports": [],
        "reports/data_validation": [],
        "reports/model_evaluation": [],
        "reports/drift_detection": [],
        "reports/performance_monitoring": [],
        
        # Pipelines
        "pipelines": [
            "__init__.py",
            "training_pipeline.py",
            "inference_pipeline.py",
            "monitoring_pipeline.py",
            "data_pipeline.py"
        ],
        
        # API structure
        "api": [
            "__init__.py",
            "app.py"
        ],
        
        "api/routes": [
            "__init__.py",
            "prediction_routes.py",
            "model_routes.py",
            "monitoring_routes.py"
        ],
        
        "api/middleware": [
            "__init__.py",
            "auth_middleware.py",
            "logging_middleware.py"
        ],
        
        # Deployment structure
        "deployment": [],
        
        "deployment/docker": [
            "training.Dockerfile",
            "serving.Dockerfile",
            "monitoring.Dockerfile"
        ],
        
        "deployment/kubernetes": [
            "training-job.yaml",
            "serving-deployment.yaml",
            "monitoring-deployment.yaml"
        ],
        
        "deployment/terraform": [
            "main.tf",
            "variables.tf",
            "outputs.tf"
        ],
        
        "deployment/scripts": [
            "deploy_model.sh",
            "setup_infrastructure.sh",
            "rollback_model.sh"
        ],
        
        # Monitoring structure
        "monitoring": ["__init__.py"],
        
        "monitoring/dashboards": [
            "grafana_dashboard.json",
            "mlflow_dashboard.py"
        ],
        
        "monitoring/alerts": [
            "drift_alerts.yaml",
            "performance_alerts.yaml"
        ],
        
        "monitoring/schedulers": [
            "__init__.py",
            "monitoring_scheduler.py",
            "retraining_scheduler.py"
        ],
        
        # Scripts
        "scripts": [
            "setup_environment.sh",
            "initialize_project.py",
            "run_training.py",
            "run_inference.py",
            "run_monitoring.py",
            "data_migration.py",
            "model_deployment.py"
        ]
    }
    
    # Create project root directory
    project_path = Path(project_name)
    project_path.mkdir(exist_ok=True)
    
    print(f"Creating MLOps project structure in: {project_path.absolute()}")
    
    # Create directories and files
    for directory, files in structure.items():
        if directory:
            dir_path = project_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {dir_path}")
        else:
            dir_path = project_path
        
        # Create empty files
        for file in files:
            file_path = dir_path / file
            file_path.touch()
            print(f"Created file: {file_path}")
    
    print(f"\n✅ MLOps project structure created successfully!")
    print(f"📁 Project location: {project_path.absolute()}")
    print(f"📊 Total directories created: {len([d for d in structure.keys() if d])}")
    print(f"📄 Total files created: {sum(len(files) for files in structure.values())}")
    
    # Create additional empty directories that might be needed
    additional_dirs = [
        "logs",
        "temp",
        ".dvc",
        "mlruns"
    ]
    
    for dir_name in additional_dirs:
        additional_path = project_path / dir_name
        additional_path.mkdir(exist_ok=True)
        print(f"Created additional directory: {additional_path}")
    
    return project_path

def create_gitignore_content(project_path):
    """Create a comprehensive .gitignore file for the MLOps project."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv/
.env

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Jupyter Notebooks
.ipynb_checkpoints

# MLflow
mlruns/
mlartifacts/

# DVC
.dvc/cache
.dvc/tmp
.dvc/plots

# Data files (let DVC handle these)
data/raw/*
data/processed/*
data/features/*
!data/raw/.gitkeep
!data/processed/.gitkeep
!data/features/.gitkeep

# Model artifacts (let DVC handle these)
models/experiments/*
models/production/*
models/staging/*
!models/experiments/.gitkeep
!models/production/.gitkeep
!models/staging/.gitkeep

# Reports (let DVC handle large reports)
reports/*/large_reports/

# Temporary files
temp/
tmp/
*.tmp

# Logs
logs/
*.log

# OS files
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local
.env.production

# Database
*.db
*.sqlite

# Spark
spark-warehouse/
derby.log
metastore_db/
"""
    
    gitignore_path = project_path / ".gitignore"
    with open(gitignore_path, 'w') as f:
        f.write(gitignore_content)
    
    print(f"Updated .gitignore with comprehensive rules")

def main():
    """Main function to create the project structure."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Create MLOps project structure")
    parser.add_argument(
        "--project-name", 
        default="mlops-classification",
        help="Name of the project directory (default: mlops-classification)"
    )
    parser.add_argument(
        "--create-gitignore",
        action="store_true",
        help="Create comprehensive .gitignore file"
    )
    
    args = parser.parse_args()
    
    # Create project structure
    project_path = create_mlops_project_structure(args.project_name)
    
    # Create .gitignore if requested
    if args.create_gitignore:
        create_gitignore_content(project_path)
    
    print(f"\n🚀 Ready to start your MLOps project!")
    print(f"📖 Next steps:")
    print(f"   1. cd {args.project_name}")
    print(f"   2. python -m venv venv")
    print(f"   3. source venv/bin/activate  # or venv\\Scripts\\activate on Windows")
    print(f"   4. pip install -r requirements.txt")
    print(f"   5. dvc init")
    print(f"   6. Start implementing your entities and services!")

if __name__ == "__main__":
    main()
