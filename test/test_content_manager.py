from migcon import content_manager


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
    content = content_manager._convert_remaining_html(test_string)
    assert content.find('href') == -1
