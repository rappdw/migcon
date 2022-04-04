from migcon.content_tree import _build_content_tree, generate_replacement_dictionary
from pathlib import Path


def test_build_content_tree():
    test_string = """# RESERO (Resero)

<div id="main-content" class="pageSection">

</div>

  
  

<div class="pageSection">

<div class="pageSectionHeader">

## Available Pages:

</div>

-   [MP0. Introduction](MP0._Introduction)
    -   [Data Cleanroom](Data_Cleanroom)
-   [MP2. Policies and Procedures](MP2._Policies_and_Procedures)
    -   [ML Platform Policies](ML_Platform_Policies)
        -   [Data Clean Room - Policies](Data_Clean_Room_-_Policies)
            -   [Policy - Changing Project Dataset
                Assignments](Policy_-_Changing_Project_Dataset_Assignments)
                -   [PROPOSED CHANGES - Policy - Changing Project
                    Dataset
                    Assignments](PROPOSED_CHANGES_-_Policy_-_Changing_Project_Dataset_Assignments)

            <!-- -->

            -   [Policy - Changing Project
                Scope/Objectives](Policy_-_Changing_Project_Scope_Objectives)

            <!-- -->

            -   [Policy - Changing Project User
                Assignments](Policy_-_Changing_Project_User_Assignments)

            <!-- -->

            -   [Policy - Customer Data in OneDrive (MS Office
                Online)](Policy_-_Customer_Data_in_OneDrive_MS_Office_Online_)

            <!-- -->

            -   [Policy - Data Science Data Handling
                Training](Policy_-_Data_Science_Data_Handling_Training)

            <!-- -->

            -   [Policy - Image Management](Policy_-_Image_Management)

            <!-- -->

            -   [Policy - Infrastructure Change
                Management](Policy_-_Infrastructure_Change_Management)

            <!-- -->

            -   [Policy - Ingesting From Data
                Platform](Policy_-_Ingesting_From_Data_Platform)

            <!-- -->

            -   [Policy - Intern Access to the
                Cleanroom](Policy_-_Intern_Access_to_the_Cleanroom)

            <!-- -->

            -   [Policy - Periodic Security
                Reviews](Policy_-_Periodic_Security_Reviews)

            <!-- -->

            -   [Policy - Project Data
                Governance](Policy_-_Project_Data_Governance)
                -   [PROPOSED CHANGES - Policy - Project Data
                    Governance](PROPOSED_CHANGES_-_Policy_-_Project_Data_Governance)

            <!-- -->

            -   [Policy - Project Security
                Controls](Policy_-_Project_Security_Controls)

            <!-- -->

            -   [Policy - Provide POC UI
                Access](Policy_-_Provide_POC_UI_Access)

            <!-- -->

            -   [Policy - Starting a New
                Project](Policy_-_Starting_a_New_Project)

            <!-- -->

            -   [Policy - Terminating a
                Project](Policy_-_Terminating_a_Project)

        <!-- -->

        -   [Inference Policies](Inference_Policies)
            -   [Policy - Operational
                Duties](Policy_-_Operational_Duties)

            <!-- -->

            -   [Release Readiness](Release_Readiness)

        <!-- -->

        -   [Policy - Backtrace a Production
            Model](Policy_-_Backtrace_a_Production_Model)

        <!-- -->

        -   [Policy - CVE Remediation](Policy_-_CVE_Remediation)

    <!-- -->

    -   [ML Platform Procedures](ML_Platform_Procedures)
        -   [Data Cleanroom - Training
            Ledger](Data_Cleanroom_-_Training_Ledger)

        <!-- -->

        -   [Data Clean Room - Playbooks](Data_Clean_Room_-_Playbooks)
            -   [Playbook - Add a Dataset to a
                Project](Playbook_-_Add_a_Dataset_to_a_Project)

            <!-- -->

            -   [Playbook - Add Clean Room User to
                Project](Playbook_-_Add_Clean_Room_User_to_Project)

            <!-- -->

            -   [Playbook - Add New Clean Room
                User](Playbook_-_Add_New_Clean_Room_User)

            <!-- -->

            -   [Playbook - Change Dataset/Model
                Classification](Playbook_-_Change_Dataset_Model_Classification)
                -   [Phission Archetype Model Reclassification
                    s3://r-phission/artifacts/prod/prod-release-v2/archetype-artifact-0.0.5-1.x86_64.rpm](Phission_Archetype_Model_Reclassification_s3_r-phission_artifacts_prod_prod-release-v2_archetype-artifact-0.0.5-1.x86_64.rpm)

                <!-- -->

                -   [Phission model reclassification after
                    cleansing](Phission_model_reclassification_after_cleansing)

                <!-- -->

                -   [Sandbox Similarity Model Artifact
                    Reclassification](Sandbox_Similarity_Model_Artifact_Reclassification)

            <!-- -->

            -   [Playbook - Create a OneDrive Document with Customer
                Information](Playbook_-_Create_a_OneDrive_Document_with_Customer_Information)

            <!-- -->

            -   [Playbook - Making Infrastructure
                Changes](Playbook_-_Making_Infrastructure_Changes)

            <!-- -->

            -   [Playbook - Monthly Security
                Review](Playbook_-_Monthly_Security_Review)

            <!-- -->

            -   [Playbook - New Project
                Creation](Playbook_-_New_Project_Creation)
                -   [TEMPLATE: User Acknowledgement
                    Tracking](TEMPLATE_User_Acknowledgement_Tracking)

            <!-- -->

            -   [Playbook - Project
                Termination](Playbook_-_Project_Termination)

            <!-- -->

            -   [Playbook - Provide Auxiliary UI
                Access](Playbook_-_Provide_Auxiliary_UI_Access)
                -   [Share Email Address Labeling Spreadsheets for
                    SCANR](Share_Email_Address_Labeling_Spreadsheets_for_SCANR)

                <!-- -->

                -   [Share POC UI for
                    camp-disco](Share_POC_UI_for_camp-disco)

                <!-- -->

                -   [Share POC UI for ML Platform
                    Docs](Share_POC_UI_for_ML_Platform_Docs)

                <!-- -->

                -   [Share POC UI for
                    PANIC/PCIP](Share_POC_UI_for_PANIC_PCIP)

                <!-- -->

                -   [Share POC UI for Phission (archetype
                    management)](Share_POC_UI_for_Phission_archetype_management_)

                <!-- -->

                -   [Share POC UI for Sandbox
                    Similarity](Share_POC_UI_for_Sandbox_Similarity)

                <!-- -->

                -   [Share UI for
                    Title-Classifier](Share_UI_for_Title-Classifier)

            <!-- -->

            -   [Playbook - Quarterly Security
                Review](Playbook_-_Quarterly_Security_Review)

            <!-- -->

            -   [Playbook - Remove Clean Room
                User](Playbook_-_Remove_Clean_Room_User)

            <!-- -->

            -   [Playbook - Remove Clean Room User from
                Project](Playbook_-_Remove_Clean_Room_User_from_Project)

            <!-- -->

            -   [Playbook - Remove Dataset from
                Project](Playbook_-_Remove_Dataset_from_Project)

            <!-- -->

            -   [Playbook - Setup New Clean Room
                Account](Playbook_-_Setup_New_Clean_Room_Account)

            <!-- -->

            -   [Playbook - Train New Cleanroom
                User](Playbook_-_Train_New_Cleanroom_User)

        <!-- -->

        -   [Inference Playbooks](Inference_Playbooks)
            -   [Playbook - First Production
                Deployment](Playbook_-_First_Production_Deployment)

            <!-- -->

            -   [Playbook - Incremental Deploy to
                Production](Playbook_-_Incremental_Deploy_to_Production)

            <!-- -->

            -   [Playbook - MLOps Backup](Playbook_-_MLOps_Backup)

        <!-- -->

        -   [Requesting Help from Batman](Requesting_Help_from_Batman)

        <!-- -->

        -   [Playbook - Support Responsibilities
            (Batman)](Playbook_-_Support_Responsibilities_Batman_)

        <!-- -->

        -   [Playbook - CVE Remediation](Playbook_-_CVE_Remediation)
-   [MP3. Operations](MP3._Operations)
    -   [Data Cleanroom Operations](Data_Cleanroom_Operations)
        -   [Creating New Images for the Docker
            Bakery](Creating_New_Images_for_the_Docker_Bakery)

        <!-- -->

        -   [Log4j CVE Response](Log4j_CVE_Response)

        <!-- -->

        -   [Playbook - Ingesting from different
            datasources](Playbook_-_Ingesting_from_different_datasources)

        <!-- -->

        -   [Stash Webhooks and
            CodePipeline](Stash_Webhooks_and_CodePipeline)

    <!-- -->

    -   [Inference Operations](Inference_Operations)
        -   [Authentication and
            Authorization](Authentication_and_Authorization)

        <!-- -->

        -   [High Volume Network
            Architecture](High_Volume_Network_Architecture)

        <!-- -->

        -   [Inference Environments - Operational
            Plan](Inference_Environments_-_Operational_Plan)

        <!-- -->

        -   [Playbook - DNS Management](Playbook_-_DNS_Management)
-   [MP5. ML Platform Shared Responsibility
    Model](MP5._ML_Platform_Shared_Responsibility_Model)
-   [MP6. ML Platform Change Process](MP6._ML_Platform_Change_Process)

</div>
"""

    source_dir = Path('/example/source/dir')
    target_dir = Path('/example/target/dir')
    result = _build_content_tree(test_string, source_dir, target_dir)
    assert result.filepath == target_dir
    assert len(result.children) == 5

    replacements = generate_replacement_dictionary(result)
    assert len(replacements) == 77
