import migcon.attachment as attachment_info


def test_processing():
    test_string = """
Thie is a test string...

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[network-firewall-design](attachments/357810050/357811162)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[network-firewall-design.png](attachments/357810050/357811163.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[network-firewall-design](attachments/357810050/357811144)
(application/vnd.jgraph.mxfile)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[network-firewall-design.png](attachments/357810050/357811145.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [Screen
Shot 2020-09-08 at 5.23.23 PM.png](attachments/357810050/357811168.png)
(image/png)  

</div>

Any further information...
    """
    info = attachment_info.process_attachment(test_string, "test")
    print(info)
    assert info.page_id == "357810050"
    assert len(info.attachments) == 3
    assert "network-firewall-design" in info.attachments
    assert "network-firewall-design.png" in info.attachments
    assert "Screen_Shot_2020-09-08_at_5.23.23_PM.png" in info.attachments
