from markdown_it import MarkdownIt

import migcon.attachment_info
from migcon import content_manager


def test_process_tokens():
    test_string = """
<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[vpc-architectures](attachments/373590217/373590285)
(application/vnd.jgraph.mxfile)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[vpc-architectures.png](attachments/373590217/373590286.png)
(image/png)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[application-capsule](attachments/373590217/373590299)
(application/vnd.jgraph.mxfile)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[application-capsule.png](attachments/373590217/373590300.png)
(image/png)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[vpc-architectures](attachments/373590217/373590296)
(application/vnd.jgraph.mxfile)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[vpc-architectures.png](attachments/373590217/373590297.png)
(image/png)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[vpc-architectures](attachments/373590217/373590220)
(application/vnd.jgraph.mxfile)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[vpc-architectures.png](attachments/373590217/373590221.png)
(image/png)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[application-capsule](attachments/373590217/373590218)
(application/vnd.jgraph.mxfile)  
<img src="/images/icons/bullet_blue.gif" width="8" height="8" />
[application-capsule.png](attachments/373590217/373590219.png)
(image/png)  

</div>
    """

    md = MarkdownIt()
    data = test_string.replace(content_manager.REMOVE_STRING_A, '').replace(content_manager.REMOVE_STRING_B, '')
    tokens = md.parse(data)
    attachment_info = migcon.attachment_info.process_tokens(tokens, "test_file")
    assert attachment_info
    assert attachment_info.page_id == "373590217"
    assert attachment_info.attachments
    assert len(attachment_info.attachments) == 4
    assert 'vpc-architectures' in attachment_info.attachments
    assert 'vpc-architectures.png' in attachment_info.attachments
    assert 'application-capsule' in attachment_info.attachments
    assert 'application-capsule.png' in attachment_info.attachments

    test_string2 = """
<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405902848.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405902847)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405902916)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405902917.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405902919)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405902920.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405902924)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405902925.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405903305)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405903306.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405904755)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405904756.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405913931)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405913932.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405913933)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405913934.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram](attachments/405902712/405902793)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [DRAFT
DLP VPC Diagram.png](attachments/405902712/405902794.png) (image/png)  

</div>
    """

    data = test_string2.replace(content_manager.REMOVE_STRING_A, '').replace(content_manager.REMOVE_STRING_B, '')
    tokens = md.parse(data)
    attachment_info = migcon.attachment_info.process_tokens(tokens, "test_file")
    assert attachment_info
    assert attachment_info.page_id == "405902712"
    assert attachment_info.attachments
    assert len(attachment_info.attachments) == 2
    assert 'DRAFT DLP VPC Diagram.png' in attachment_info.attachments
    assert 'DRAFT DLP VPC Diagram' in attachment_info.attachments

    test_string3 = """
<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[\<Project ID\>.\<Cycle Number\> - \<Project
Name\>.json](attachments/443510468/443510469.json)
(application/octet-stream)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/451022695.json)
(application/json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/451022696.json)
(application/octet-stream)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/451022697.json)
(application/octet-stream)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/451022698.json)
(application/octet-stream)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/451022699.json)
(application/octet-stream)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/451028119.json)
(application/octet-stream)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/451028121.json)
(application/octet-stream)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/451028124.json)
(application/octet-stream)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [PL.05 -
Improve ML Platform
Documentation.json](attachments/443510468/443510478.json)
(application/octet-stream)  

</div>
    """

    data = test_string3.replace(content_manager.REMOVE_STRING_A, '').replace(content_manager.REMOVE_STRING_B, '')
    tokens = md.parse(data)
    attachment_info = migcon.attachment_info.process_tokens(tokens, "test_file")
    assert attachment_info
    assert attachment_info.page_id == "443510468"
    assert attachment_info.attachments
    assert len(attachment_info.attachments) == 2
    count = 0
    for attachment in attachment_info.attachments.values():
        for files in attachment.files.values():
            count += len(files)
    assert count == 10

def test_div_fixups():
    test_string = """
<td class="confluenceTd"><div class="content-wrapper">
<div class="content-wrapper">
<p>NOT STARTED</p>
</div>
</div></td>
"""
    new = content_manager._fixup_divs(test_string)
    assert new.find('<div class="content-wrapper">') == -1

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
    content = content_manager.fixup_toc_macro(test_string)
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
    content = content_manager.fixup_expander(test_string)
    assert content.find('expander-') == -1


