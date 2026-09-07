import importlib
import pkgutil
import submissions


def main() -> None:
    for module_info in pkgutil.iter_modules(submissions.__path__):
        module_name = module_info.name

        if module_name.startswith("_"):
            continue

        full_module_name = f"submissions.{module_name}"

        try:
            module = importlib.import_module(full_module_name)

            if not hasattr(module, "run"):
                print(f"{module_name}: missing run() function")
                continue

            result = module.run()
            print(f"{module_name}: {result}")

        except Exception as error:
            print(f"{module_name}: ERROR - {error}")


if __name__ == "__main__":
    main()