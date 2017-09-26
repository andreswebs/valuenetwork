#
# Process: An activity that changes inputs into outputs.  It could transform or transport EconomicResource(s).
#

import graphene
from graphene_django.types import DjangoObjectType
import valuenetwork.api.types as types
from valuenetwork.api.types.EconomicEvent import Action
from valuenetwork.valueaccounting.models import Process as ProcessProxy, EventType, ProcessType
from valuenetwork.api.models import formatAgent


class ProcessClassification(DjangoObjectType):
    note = graphene.String(source='note')
    scope = graphene.Field(lambda: types.Agent)
    estimated_duration = graphene.String(source='estimated_duration') #in minutes

    class Meta:
        model = ProcessType
        only_fields = ('id', 'name')

    def resolve_scope(self, args, *rargs):
        return formatAgent(self.scope)


class Process(DjangoObjectType):
    scope = graphene.Field(lambda: types.Agent)
    planned_start = graphene.String(source='planned_start')
    planned_duration = graphene.String(source='planned_duration')
    is_started = graphene.Boolean(source='is_started')
    is_finished = graphene.Boolean(source='is_finished')
    process_classified_as = graphene.Field(ProcessClassification)
    note = graphene.String(source='note')

    class Meta:
        model = ProcessProxy
        only_fields = ('id', 'name')

    inputs = graphene.List(lambda: types.EconomicEvent,
                                        action=Action()) #VF

    outputs = graphene.List(lambda: types.EconomicEvent,
                            action=Action()) #VF

    unplanned_economic_events = graphene.List(lambda: types.EconomicEvent,
                                              action=Action())

    committed_inputs = graphene.List(lambda: types.Commitment,
                                     action=Action()) #VF

    committed_outputs = graphene.List(lambda: types.Commitment,
                                      action=Action()) #VF

    next_processes = graphene.List(lambda: types.Process)

    previous_processes = graphene.List(lambda: types.Process)

    working_agents = graphene.List(lambda: types.Agent)
    
    process_plan = graphene.Field(lambda: types.Plan)

    #next_resource_taxonomy_items = graphene.List(lambda: types.ResourceTaxonomyItem)

    #previous_resource_taxonomy_items = graphene.List(lambda: types.ResourceTaxonomyItem)

    #resource_classifications_by_action = graphene.List(lambda: types.ResourceClassification)


    def resolve_scope(self, args, *rargs):
        return formatAgent(self.scope)

    def resolve_process_plan(self, args, *rargs):
        return self.independent_demand()

    def resolve_process_classified_as(self, args, *rargs):
        return self.process_type

    def resolve_inputs(self, args, context, info):
        action = args.get('action')
        events = self.incoming_events()
        if action:
            event_type = EventType.objects.convert_action_to_event_type(action)
            events = events.filter(event_type=event_type)
        return events

    def resolve_outputs(self, args, context, info):
        action = args.get('action')
        events = self.outputs()
        if action:
            event_type = EventType.objects.convert_action_to_event_type(action)
            events = events.filter(event_type=event_type)
        return events

    def resolve_committed_inputs(self, args, context, info):
        action = args.get('action')
        commits = self.incoming_commitments()
        if action:
            event_type = EventType.objects.convert_action_to_event_type(action)
            commits = commits.filter(event_type=event_type)
        return commits

    def resolve_committed_outputs(self, args, context, info):
        action = args.get('action')
        commits = self.outgoing_commitments()
        if action:
            event_type = EventType.objects.convert_action_to_event_type(action)
            commits = commits.filter(event_type=event_type)
        return commits

    def resolve_next_processes(self, args, context, info):
        return self.next_processes()

    def resolve_previous_processes(self, args, context, info):
        return self.previous_processes()

    def resolve_working_agents(self, args, context, info):
        agents = self.all_working_agents()
        formatted_agents = []
        for agent in agents:
            formatted_agents.append(formatAgent(agent))
        return formatted_agents

    def resolve_unplanned_economic_events(self, args, context, info):
        action = args.get('action')
        unplanned_events = self.uncommitted_events()
        if action:
            event_type = EventType.objects.convert_action_to_event_type(action)
            unplanned_events = unplanned_events.filter(event_type=event_type)
        return unplanned_events

    #def resolve_next_resource_taxonomy_items(self, args, context, info):
    #    return self.output_resource_types()

    #def resolve_previous_resource_taxonomy_items(self, args, context, info):
    #    return self.

    #def resolve_resource_classifications_by_action(self, args, context, info): #TODO not completed
    #    action = args.get('action')
    #    if action:
    #        event_type = action._convert_action_to_event_type()
    #        return self.get_rts_by_action(event_type)
    #    return None