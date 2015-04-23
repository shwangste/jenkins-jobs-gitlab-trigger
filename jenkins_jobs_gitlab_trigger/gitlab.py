import xml.etree.ElementTree as XML


def gitlab_triggers(parser, xml_parent, data):
    """yaml: gitlab

    Example::

      triggers:
        - gitlab:
            when-push: true
            when-mr: true
            when-push-on-mr: true
            set-desc: true
            add-note-on-mr: true
            allow-all-branches: true
    """
    if data is None:
        data = dict()

    trigger = XML.SubElement(
        xml_parent, 'com.dabsquared.gitlabjenkins.GitLabPushTrigger')
    trigger.set('plugin', 'gitlab-plugin@1.1.15')

    XML.SubElement(trigger, 'spec').text = ''

    for opt, attr in (('when-push', 'triggerOnPush'),
                      ('when-mr', 'triggerOnMergeRequest'),
                      ('when-push-on-mr', 'triggerOpenMergeRequestOnPush'),
                      ('set-desc', 'setBuildDescription'),
                      ('add-note-on-mr', 'addNoteOnMergeRequest'),
                      ('allow-all-branches', 'allowAllBranches')):
        (XML.SubElement(trigger, attr)
         .text) = 'true' if data.get(opt, True) else 'false'
        
    XML.SubElement(trigger, 'allowedBranches').text = ''
