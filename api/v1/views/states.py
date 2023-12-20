#!/usr/bin/python3
"""State Model View"""

from models import storage
from models.state import State
from flask import Flask, jsonify, Response
from api.v1.views import app_views

all_states = storage.all(State)

@app_views.get('/states')
def stateAll():
    """GET route to return all States"""
    all_states_arr = [obj.to_dict() for obj in all_states.values()]
    return jsonify(all_states_arr)

@app_views.get('/states/<state_id>')
def stateId(state_id):
    """GET route to return one specific State"""
    try:
        state = all_states[f'State.{state_id}']
        return state.to_dict()
    except KeyError:
        from flask import abort
        return abort(404)

@app_views.delete('/states/<state_id>')
def deleteStateId(state_id):
    """DELETE route to delete a State"""
    try:
        state = all_states[f'State.{state_id}']
        print(state)
        storage.delete(state)
        return Response(jsonify({}), status=200)
    except KeyError:
        from flask import abort
        return abort(404)
