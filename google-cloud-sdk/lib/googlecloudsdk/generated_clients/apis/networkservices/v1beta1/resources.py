# -*- coding: utf-8 -*- #
# Copyright 2023 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Resource definitions for Cloud Platform Apis generated from apitools."""

import enum


BASE_URL = 'https://networkservices.googleapis.com/v1beta1/'
DOCS_URL = 'https://cloud.google.com/networking'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  PROJECTS = (
      'projects',
      'projects/{projectsId}',
      {},
      ['projectsId'],
      True
  )
  PROJECTS_LOCATIONS = (
      'projects.locations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_AUTHZEXTENSIONS = (
      'projects.locations.authzExtensions',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/authzExtensions/'
              '{authzExtensionsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_ENDPOINTPOLICIES = (
      'projects.locations.endpointPolicies',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'endpointPolicies/{endpointPoliciesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_GATEWAYS = (
      'projects.locations.gateways',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/gateways/'
              '{gatewaysId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_GATEWAYS_ROUTEVIEWS = (
      'projects.locations.gateways.routeViews',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/gateways/'
              '{gatewaysId}/routeViews/{routeViewsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_GRPCROUTES = (
      'projects.locations.grpcRoutes',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/grpcRoutes/'
              '{grpcRoutesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_HTTPROUTES = (
      'projects.locations.httpRoutes',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/httpRoutes/'
              '{httpRoutesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_LBEDGEEXTENSIONS = (
      'projects.locations.lbEdgeExtensions',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'lbEdgeExtensions/{lbEdgeExtensionsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_LBROUTEEXTENSIONS = (
      'projects.locations.lbRouteExtensions',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'lbRouteExtensions/{lbRouteExtensionsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_LBTRAFFICEXTENSIONS = (
      'projects.locations.lbTrafficExtensions',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'lbTrafficExtensions/{lbTrafficExtensionsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MESHES = (
      'projects.locations.meshes',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/meshes/'
              '{meshesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MESHES_ROUTEVIEWS = (
      'projects.locations.meshes.routeViews',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/meshes/'
              '{meshesId}/routeViews/{routeViewsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTCONSUMERASSOCIATIONS = (
      'projects.locations.multicastConsumerAssociations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastConsumerAssociations/'
              '{multicastConsumerAssociationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTDOMAINACTIVATIONS = (
      'projects.locations.multicastDomainActivations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastDomainActivations/{multicastDomainActivationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTDOMAINGROUPS = (
      'projects.locations.multicastDomainGroups',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastDomainGroups/{multicastDomainGroupsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTDOMAINS = (
      'projects.locations.multicastDomains',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastDomains/{multicastDomainsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTGROUPCONSUMERACTIVATIONS = (
      'projects.locations.multicastGroupConsumerActivations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastGroupConsumerActivations/'
              '{multicastGroupConsumerActivationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTGROUPPRODUCERACTIVATIONS = (
      'projects.locations.multicastGroupProducerActivations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastGroupProducerActivations/'
              '{multicastGroupProducerActivationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTGROUPRANGEACTIVATIONS = (
      'projects.locations.multicastGroupRangeActivations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastGroupRangeActivations/'
              '{multicastGroupRangeActivationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTGROUPRANGES = (
      'projects.locations.multicastGroupRanges',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastGroupRanges/{multicastGroupRangesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_MULTICASTPRODUCERASSOCIATIONS = (
      'projects.locations.multicastProducerAssociations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'multicastProducerAssociations/'
              '{multicastProducerAssociationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_OPERATIONS = (
      'projects.locations.operations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/operations/'
              '{operationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_SERVICEBINDINGS = (
      'projects.locations.serviceBindings',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/serviceBindings/'
              '{serviceBindingsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_SERVICELBPOLICIES = (
      'projects.locations.serviceLbPolicies',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'serviceLbPolicies/{serviceLbPoliciesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_TCPROUTES = (
      'projects.locations.tcpRoutes',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/tcpRoutes/'
              '{tcpRoutesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_TLSROUTES = (
      'projects.locations.tlsRoutes',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/tlsRoutes/'
              '{tlsRoutesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_WASMPLUGINS = (
      'projects.locations.wasmPlugins',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/wasmPlugins/'
              '{wasmPluginsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_WASMPLUGINS_VERSIONS = (
      'projects.locations.wasmPlugins.versions',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/wasmPlugins/'
              '{wasmPluginsId}/versions/{versionsId}',
      },
      ['name'],
      True
  )

  def __init__(self, collection_name, path, flat_paths, params,
               enable_uri_parsing):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
    self.enable_uri_parsing = enable_uri_parsing
