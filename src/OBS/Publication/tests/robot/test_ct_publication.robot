# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s OBS.Publication -t test_publication.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src OBS.Publication.testing.OBS_PUBLICATION_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/OBS/Publication/tests/robot/test_publication.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Publication
  Given a logged-in site administrator
    and an add Publication form
   When I type 'My Publication' into the title field
    and I submit the form
   Then a Publication with the title 'My Publication' has been created

Scenario: As a site administrator I can view a Publication
  Given a logged-in site administrator
    and a Publication 'My Publication'
   When I go to the Publication view
   Then I can see the Publication title 'My Publication'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Publication form
  Go To  ${PLONE_URL}/++add++Publication

a Publication 'My Publication'
  Create content  type=Publication  id=my-publication  title=My Publication

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Publication view
  Go To  ${PLONE_URL}/my-publication
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Publication with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Publication title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
