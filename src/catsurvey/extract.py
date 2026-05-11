# SPDX-FileCopyrightText: 2025-present Christopher Soria <chrissoria@berkeley.edu>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import catstack

from ._utils import build_survey_description


def extract(
    input_data,
    api_key,
    survey_question="",
    description="",
    **kwargs,
):
    """Discover categories from survey responses using LLMs.

    Thin wrapper around catstack.extract() that injects survey-specific
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
        All other arguments are passed through to catstack.extract().

    Returns
    -------
    dict
        Dictionary with 'counts_df', 'top_categories', and 'raw_top_text'.
    """
    desc = build_survey_description(survey_question, description)
    return catstack.extract(
        input_data,
        api_key,
        survey_question=desc,
        **kwargs,
    )
