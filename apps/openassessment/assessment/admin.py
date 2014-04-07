import json

from django.contrib import admin
from django.utils import html

from openassessment.assessment.models import (
    Assessment, AssessmentPart, AssessmentFeedback, AssessmentFeedbackOption,
    Criterion, CriterionOption, Rubric,
    PeerWorkflow, PeerWorkflowItem,
)

from openassessment.assessment.serializers import RubricSerializer

class RubricAdmin(admin.ModelAdmin):
    """
    Does this say anything?
    """
    list_per_page = 20

    list_display = ('id', 'content_hash', 'criteria_summary')
    list_display_links = ('id', 'content_hash')
    search_fields = ('id', 'content_hash')
    readonly_fields = (
        'id', 'content_hash', 'points_possible', 'criteria_summary', 'data'
    )

    def data(self, rubric_obj):
        rubric_data = RubricSerializer.serialized_from_cache(rubric_obj)
        return u"<pre>\n{}\n</pre>".format(
            html.escape(json.dumps(rubric_data, sort_keys=True, indent=4))
        )

    def criteria_summary(self, rubric_obj):
        rubric_data = RubricSerializer.serialized_from_cache(rubric_obj)
        return u", ".join(
            u"{}: {}".format(criterion["name"], criterion["points_possible"])
            for criterion in rubric_data["criteria"]
        )

    data.allow_tags = True

admin.site.register(Rubric, RubricAdmin)

admin.site.register(Assessment)
admin.site.register(AssessmentPart)
admin.site.register(AssessmentFeedback)
admin.site.register(AssessmentFeedbackOption)
admin.site.register(Criterion)
admin.site.register(CriterionOption)
admin.site.register(PeerWorkflow)
admin.site.register(PeerWorkflowItem)
