import difflib


def get_text_diff(before: str, after: str) -> dict:
    """
        get the change set between two strings
    """
    default_output = {
        "add": [],
        "delete": []
    }
    for i, s in enumerate(difflib.ndiff(before, after)):
        if s[0] == " ":
            continue
        elif s[0] == '-':
            default_output["delete"].append((i, s[-1],))
        else:
            default_output["add"].append((i, s[-1],))

    return default_output