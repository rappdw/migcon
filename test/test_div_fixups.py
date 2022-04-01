import migcon.div_fixups


def test_fixup_toc_macro():
    test_string = """
<div class="toc-macro rbtoc1648571394609">

- 1 [Introduction](#GeneralizedDataIngest-Introduction)
- 2 [Background](#GeneralizedDataIngest-Background)
- 3 [Proposal](#GeneralizedDataIngest-Proposal)
- 4 [Architecture Diagram](#GeneralizedDataIngest-ArchitectureDiagram)
- 5 [Supported Ingest
Types](#GeneralizedDataIngest-SupportedIngestTypes)
- 5.1 [Scheduled Job](#GeneralizedDataIngest-ScheduledJob)
- 5.2 [On-Demand Copy](#GeneralizedDataIngest-On-DemandCopy)
- 5.3 [SFTP Ingest](#GeneralizedDataIngest-SFTPIngest)
- 6 [Ingest Bucket](#GeneralizedDataIngest-IngestBucket)
- 7 [Migration](#GeneralizedDataIngest-Migration)
- 8 [Change History](#GeneralizedDataIngest-ChangeHistory)

</div>

## Introduction

This page contains a proposal for a generalized data ingest solution.
"""
    content = migcon.div_fixups.fixup_toc_macro(test_string)
    assert content.find('toc-macro') == -1
    assert content.find('Change History') == -1
    assert content.find('This page contains a proposal for a generalized data ingest solution.') != -1


def test_fixup_expander():
    test_string = """
# Inference Environment Architecture Details

<div class="contentLayout2">

<div class="columnLayout single" layout="single">

<div class="cell normal" data-type="normal">

<div class="innerCell">

# Overview

## High Level Description

<div id="expander-269883941" class="expand-container">

<div id="expander-control-269883941" class="expand-control">

<img src="/images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Click here for service description

</div>

<div id="expander-content-269883941" class="expand-content">

The ML Platform Inference Environment provides a place to run multiple
machine learning (ML)-based workloads. The ML models used in this
environment are produced by data scientists working on production data
in the Data Cleanroom.

These models are exposed on the ML Platform as internal REST APIs that
are consumable by other Proofpoint products to add ML capabilities into
their current offerings.

The ML Platform deploys workloads consumed by multiple business units
across the entire company.

</div>

</div>

</div>

</div>

</div>

"""
    content = migcon.div_fixups.fixup_expander(test_string)
    assert content.find('expander-') == -1


def test_div_fixup():
    test_string = """
## General

<div class="table-wrap">

<table class="wrapped confluenceTable">
<tbody>
<tr class="odd">
<th class="confluenceTh"><div class="content-wrapper">
<p>Product</p>
<div id="expander-638174472" class="expand-container">
<div id="expander-control-638174472" class="expand-control">
<img src="/images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Examples
</div>
<div id="expander-content-638174472" class="expand-content">
<p>PPS, TAP, Archiving, Governance, etc.</p>
</div>
</div>
<p><br />
</p>
<p><br />
</p>
</div></th>
<td class="confluenceTd">Multiple Products</td>
</tr>
<tr class="even">
<th class="confluenceTh"><div class="content-wrapper">
<p>Service Type</p>
<div id="expander-1795523471" class="expand-container">
<div id="expander-control-1795523471" class="expand-control">
<img src="/images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Examples
</div>
<div id="expander-content-1795523471" class="expand-content">
<p>Platform Java Service, Platform Rails Application, etc.</p>
</div>
</div>
</div></th>
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

</div>
"""
    content = migcon.div_fixups.fixup_divs(test_string)
    assert content.find('<div') == -1
    assert content.find('</div') == -1