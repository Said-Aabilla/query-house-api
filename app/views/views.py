import json
import logging

from django.http import JsonResponse

logging.basicConfig(level=logging.DEBUG)
from django.shortcuts import get_object_or_404,get_list_or_404
from app.models import Table, Attribute,Query,Selection
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.db.models import Avg, Count,Max
class TreeView(APIView):
    def get(self, request):
        resultSAP = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='sa',).values('projections__projection').annotate(
            avg_execution_time= Avg('execution_time_hybride'),
        )
        resultIIP = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='ii', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultRTOSP = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='RTOS', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultMINSELP = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='minSel', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultMCTSP = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='mcts', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        ##################
        resultSAPE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='sa', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        resultIIPE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='ii', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        resultRTOSPE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='RTOS', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        resultMINSELPE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='minSel', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        resultMCTSPE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='mcts', ).values('projections__projection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        ###################
        resultSAS = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='sa', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultIIS = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='ii', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultRTOSS = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='RTOS', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultMINSELS = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='minSel', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultMCTSS = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='mcts', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultSAS = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='sa', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        #############################
        resultIISE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='ii', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        resultRTOSSE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='RTOS', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        resultMINSELSE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='minSel', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        resultMCTSSE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='mcts', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )
        resultSASE = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='sa', ).values('selections__selection').annotate(
            avg_execution_time=Avg('execution_energy_hybrid'),
        )

        ########################
        resultSAJ = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='sa', ).values('number_join').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultIIJ = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='ii', ).values('number_join').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultRTOSJ = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='rtos', ).values('number_join').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultMINSELJ = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='minSel', ).values('number_join').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        resultMCTSJ = Query.objects.exclude(execution_time_hybride=-1).filter(prefix_algo='mcts', ).values('number_join').annotate(
            avg_execution_time=Avg('execution_time_hybride'),
        )
        ######################
        context = {
            'resultSAP': json.dumps(list(resultSAP)),
            'resultIIP': json.dumps(list(resultIIP)),
            'resultRTOSP': json.dumps(list(resultRTOSP)),
            'resultMINSELP': json.dumps(list(resultMINSELP)),
            'resultMCTSP': json.dumps(list(resultMCTSP)),
            ##
            'resultSAS': json.dumps(list(resultSAS)),
            'resultIIS': json.dumps(list(resultIIS)),
            'resultRTOSS': json.dumps(list(resultRTOSS)),
            'resultMINSELS': json.dumps(list(resultMINSELS)),
            'resultMCTSS': json.dumps(list(resultMCTSS)),
            ##
            'resultSASE': json.dumps(list(resultSASE)),
            'resultIISE': json.dumps(list(resultIISE)),
            'resultRTOSSE': json.dumps(list(resultRTOSSE)),
            'resultMINSELSE': json.dumps(list(resultMINSELSE)),
            'resultMCTSSE': json.dumps(list(resultMCTSSE)),
            ##
            'resultSAPE': json.dumps(list(resultSAPE)),
            'resultIIPE': json.dumps(list(resultIIPE)),
            'resultRTOSPE': json.dumps(list(resultRTOSPE)),
            'resultMINSELPE': json.dumps(list(resultMINSELPE)),
            'resultMCTSPE': json.dumps(list(resultMCTSPE)),

            ####
            'resultSAJ': json.dumps(list(resultSAJ)),
            'resultIIJ': json.dumps(list(resultIIJ)),
            'resultRTOSJ': json.dumps(list(resultRTOSJ)),
            'resultMINSELJ': json.dumps(list(resultMINSELJ)),
            'resultMCTSJ': json.dumps(list(resultMCTSJ)),
        }
        return render(request, 'chart.html', context)
        # Return the result as a JSON response
def findAttributeByNameAndTable(request, table_name, attribute_name):
    table = get_object_or_404(Table, name=table_name)
    attribute = get_object_or_404(Attribute, name=attribute_name, table=table)
    data = {
        'name': attribute.name,
        'table': attribute.table.id,
        'attribute_id': attribute.id
    }
    return JsonResponse(data)
def findTableByName(request, table_name, ):

    table = get_object_or_404(Table, name=table_name)
    data = {
        'table_id': table.id,
        'table_name': table_name,
    }
    return JsonResponse(data)