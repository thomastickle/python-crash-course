###################
# Prints a list of models saving printed models to an output list
###################
def printing_models(unprinted_designs: list[str]) -> list[str]:
    completed_models = []
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    return completed_models
