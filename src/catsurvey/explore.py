# SPDX-FileCopyrightText: 2025-present Christopher Soria <chrissoria@berkeley.edu>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import catstack

from ._utils import build_survey_description


def explore(
    input_data,
    api_key,
    survey_question="",
    description="",
    **kwargs,
):
    """Explore raw categories from survey responses (no deduplication).

    Thin wrapper around catstack.explore() that injects survey-specific
    prompt framing ("A respondent was asked: ...") into the description.

    Parameters
    ----------
    input_data : list[str] or str
        Survey responses to analyze.
    api_key : str
        API key for the LLM provider.
    survey_question : str
        The survey question that respondents answered.
    description : str
        Additional context about the survey or responses.
    **kwargs
        All other arguments are passed through to catstack.explore().

    Returns
    -------
    list[str]
        Raw list of categories (with duplicates across iterations).
    """
    desc = build_survey_description(survey_question, description)
    return catstack.explore(
        input_data,
        api_key,
        description=desc,
        domain="survey",
        **kwargs,
    )
