# SPDX-FileCopyrightText: 2025-present Christopher Soria <chrissoria@berkeley.edu>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import catstack

from ._utils import build_survey_description


def classify(
    input_data,
    categories,
    survey_question="",
    description="",
    add_other="prompt",
    check_verbosity=True,
    **kwargs,
):
    """Classify survey responses into categories using LLMs.

    Thin wrapper around catstack.classify() that injects survey-specific
    prompt framing ("A respondent was asked: ...") into the description.

    Parameters
    ----------
    input_data : list[str] or str
        Survey responses to classify (list of text, image dir, or PDF dir).
    categories : list[str]
        Category names for classification.
    survey_question : str
        The survey question that respondents answered.
    description : str
        Additional context about the survey or responses.
    add_other : str or bool
        Whether to add an "Other" category. Default "prompt".
    check_verbosity : bool
        Whether to check category verbosity. Default True.
    **kwargs
        All other arguments are passed through to catstack.classify().

    Returns
    -------
    pd.DataFrame
        Classification results.
    """
    desc = build_survey_description(survey_question, description)
    return catstack.classify(
        input_data,
        categories,
        description=desc,
        add_other=add_other,
        check_verbosity=check_verbosity,
        **kwargs,
    )
