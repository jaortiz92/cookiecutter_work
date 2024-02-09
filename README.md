## Directories

```
├── .gitignore                                  <- GitHub's excellent Python .gitignore customized for this project
├── main.py                                     <- File to run the project
├── README.md                                   <- The top-level README for developers using this project.
├── requirements.txt                            <- The requirements file for reproducing the analysis environment, e.g.
│                                                   generated with `pip freeze > requirements.txt`
│
├── data
│   ├── external                                <- Data from third party sources.
│   ├── interim                                 <- Intermediate data that has been transformed.
│   ├── processed                               <- The final, canonical data sets for modeling.
│   └── raw                                     <- The original, own data without modifications.
│
├── docs                                        <- A default space to add documentation, manuals, and all other explanatory materials
│
├── models                                      <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks                                   <- Jupyter notebooks. Naming convention is a number (for ordering),
│                                                   the creator's initials, and a short `-` delimited description, e.g.
│                                                   `1.0-jqp-initial-data-exploration`.
│
├── reports                                     <- Generated analysis as HTML, PDF, LaTeX, etc.
│
│
└── {{ cookiecutter.project_module_name }}      <- Source code for use in this project.
    ├── __init__.py                             <- Makes {{ cookiecutter.project_module_name }} a Python module.
    │
    ├──{{ cookiecutter.project_module_name }}.py<- File with main class
    │
    ├── models                                  <- Scripts to train models and then use trained models to make
    │                                               predictions.
    │
    ├── utils                                   <- Scripts to help with common tasks.
    │   ├── __init__.py                         <- Makes a Python module.
    │   ├── constants.py                        <- Variables constansts
    │   ├── paths.py                            <- Helper functions to relative file referencing across project.
    │   ├── utils.py                            <- General functions required
    │
    └── visualization                           <- Scripts to create exploratory and results oriented visualizations.
    │   ├── __init__.py                         <- Makes a Python module.
        └── visualize.py                        <- Functions to do visualizations

```