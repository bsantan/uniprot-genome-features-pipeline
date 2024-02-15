


def initialize_robot(path: str) -> list:
    """
    Initialize ROBOT with necessary configuration.

    :param path: Path to ROBOT files.
    :return: A list consisting of robot shell script name and environment variables.
    """
    # Declare variables
    robot_file = os.path.join(path, "robot")

    # Declare environment variables
    env = dict(os.environ)
    # (JDK compatibility issue:
    # https://stackoverflow.com/questions/49962437/unrecognized-vm-option-useparnewgc-error-could-not-create-the-java-virtual) # noqa
    # env['ROBOT_JAVA_ARGS'] = '-Xmx8g -XX:+UseConcMarkSweepGC' # for JDK 9 and older
    env["ROBOT_JAVA_ARGS"] = "-Xmx12g -XX:+UseG1GC"  # For JDK 10 and over
    env["PATH"] = os.environ["PATH"]
    env["PATH"] += os.pathsep + path

    return [robot_file, env]



def remove_convert_to_json(path: str, ont_name: str, terms: Union[List, Path]):
    """
    Remove all children of provided CURIE(s).

    :param path: path of file to be converted
    :param ont_name: Name of the ontology
    :param terms: Either CURIE or a file of CURIEs list.
    :return: None
    """
    robot_file, env = initialize_robot(path)
    input_owl = os.path.join(path, ont_name.lower() + ".owl")
    output_json = os.path.join(path, ont_name.lower() + ROBOT_REMOVED_SUFFIX + ".json")

    input_file = input_owl

    if isinstance(terms, List):
        terms_param = [
            item for sublist in zip(["--term"] * len(terms), terms) for item in sublist  # noqa
        ]
        call = [
            "bash",
            robot_file,
            "remove",
            "--input",
            input_file,
            *terms_param,
            "--select",
            "'self descendants'",
            "convert",
            "--output",
            output_json,
        ]
    else:
        call = [
            "bash",
            robot_file,
            "remove",
            "--input",
            input_file,
            "--term-file",
            terms,
            "--select",
            "'self descendants'",
            "convert",
            "--output",
            output_json,
        ]

    subprocess.call(call, env=env)  # noqa

    return None

