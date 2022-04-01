import migcon.link_and_table_handler

def test_convert_html():
    test_string = """
## General

<table class="wrapped confluenceTable">
<tbody>
<tr class="odd">
<th class="confluenceTh"><p>Product</p>

```{dropdown} Examples
<p>PPS, TAP, Archiving, Governance, etc.</p>
```
<p><br />
</p>
<p><br />
</p>
</th>
<td class="confluenceTd">Multiple Products</td>
</tr>
<tr class="even">
<th class="confluenceTh"><p>Service Type</p>

```{dropdown} Examples
<p>Platform Java Service, Platform Rails Application, etc.</p>
```
</th>
<td class="confluenceTd"><p>Multiple AWS Services hosting primarily
Python REST APIs.</p></td>
</tr>
<tr class="odd">
<th class="confluenceTh"><p>Puppet Class</p></th>
<td class="confluenceTd">N/A</td>
</tr>
<tr class="even">
<th class="confluenceTh"><p>Service Record</p></th>
<td class="confluenceTd">N/A</td>
</tr>
<tr class="odd">
<th class="confluenceTh"><p>Link to Build Job on Jenkins</p></th>
<td class="confluenceTd">N/A</td>
</tr>
<tr class="even">
<th class="confluenceTh">Link to API Documentation</th>
<td class="confluenceTd">N/A</td>
</tr>
<tr class="odd">
<th class="confluenceTh"><p>Source Repository (name of git
repository)</p></th>
<td class="confluenceTd"><p><a
href="https://hq-stash.corp.proofpoint.com/projects/RESEROIAC/repos/inference-infrastructure/browse"
rel="nofollow">Browse ReseroIAC / inference-infrastructure - HQ Stash
Bitbucket (proofpoint.com)</a></p>
<p><a
href="https://hq-stash.corp.proofpoint.com/projects/RESEROIAC/repos/inference-service-modules/browse"
rel="nofollow">Browse ReseroIAC / inference-service-modules - HQ Stash
Bitbucket (proofpoint.com)</a></p></td>
</tr>
<tr class="even">
<th class="confluenceTh"><p>Engineering Team's Email Alias</p></th>
<td class="confluenceTd">OG-mllabsengineering@proofpoint.com</td>
</tr>
<tr class="odd">
<th class="confluenceTh"><p>Product Owner</p></th>
<td class="confluenceTd">Dan Rapp</td>
</tr>
<tr class="even">
<th class="confluenceTh"><p>Operations Service Owner</p></th>
<td class="confluenceTd"><br />
</td>
</tr>
<tr class="odd">
<th class="confluenceTh">Link to corresponding Resiliency Checklist</th>
<td class="confluenceTd"><br />
</td>
</tr>
</tbody>
</table>
"""
    content = migcon.link_and_table_handler.convert_remaining_html(test_string)
    assert content.find('href') == -1


def test_fixup_md_table():
    test_string = """
| Step | Who | What |
| --- | --- | --- |
| 1 | P | Ensure user has been trained on cleanroom
rules. If the individual is not listed as a trained user on [this page](https://wiki.proofpoint.com/wiki/display/RESERO/Data+Cleanroom+-+Training+Ledger), run [this playbook](https://wiki.proofpoint.com/wiki/pages/viewpage.action?pageId=304064753). |
| 2 | P | * Find the project's User Approvals JIRA ticket, it should be linked
on the Governing Proposal.
* Send the user a link to the ticket and ask them to read the
description and follow the instructions there.
* After user has provided written acknowledgement on ticket, assign
the card to M.
 |
| 3 | M | Manager reviews and approves/denies the request
in a comment on the JIRA ticket |
| 4 | E | * Add the user to the project's terraform user list
* Notify project team of completion
 |
| 4 | P | Update the project's Governing Proposal by
adding the user to the Clean Room Project Personnel table. |
    """

    result = migcon.link_and_table_handler.fixup_table_md(test_string)

    expected_result = """| Step | Who | What |
| --- | --- | --- |
| 1 | P | Ensure user has been trained on cleanroom rules. If the individual is not listed as a trained user on [this page](https://wiki.proofpoint.com/wiki/display/RESERO/Data+Cleanroom+-+Training+Ledger), run [this playbook](https://wiki.proofpoint.com/wiki/pages/viewpage.action?pageId=304064753). |
| 2 | P | * Find the project's User Approvals JIRA ticket, it should be linked on the Governing Proposal.<br />* Send the user a link to the ticket and ask them to read the description and follow the instructions there.<br />* After user has provided written acknowledgement on ticket, assign the card to M. |
| 3 | M | Manager reviews and approves/denies the request in a comment on the JIRA ticket |
| 4 | E | * Add the user to the project's terraform user list<br />* Notify project team of completion |
| 4 | P | Update the project's Governing Proposal by adding the user to the Clean Room Project Personnel table. |"""

    assert len(result.split('\n')) == 7
    assert result == expected_result

