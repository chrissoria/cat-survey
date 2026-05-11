# SPDX-FileCopyrightText: 2025-present Christopher Soria <chrissoria@berkeley.edu>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import catstack


def summarize(input_data, **kwargs):
    """Summarize survey responses using LLMs.

    Pure pass-through to catstack.summarize().

    Parameters
    ----------
    input_data : list[str], str, or PDF directory
        Survey responses or documents to summarize.
    **kwargs
        All arguments are passed through to catstack.summarize().

    Returns
    -------
    pd.DataFrame
        Summarization results.
    """
    return catstack.summarize(input_data, **kwargs)
