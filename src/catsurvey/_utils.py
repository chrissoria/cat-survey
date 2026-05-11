# SPDX-FileCopyrightText: 2025-present Christopher Soria <chrissoria@berkeley.edu>
#
# SPDX-License-Identifier: GPL-3.0-or-later


def build_survey_description(survey_question, description=""):
    """Build a survey-framed description string.

    Combines the survey question and optional description into a single
    string with survey-specific framing.

    Parameters
    ----------
    survey_question : str
        The survey question that respondents answered.
    description : str
        Additional context about the survey or responses.

    Returns
    -------
    str
        Combined description with survey framing.
    """
    parts = []
    if survey_question:
        parts.append(f"A respondent was asked: '{survey_question}'.")
    if description:
        parts.append(description)
    return " ".join(parts)
