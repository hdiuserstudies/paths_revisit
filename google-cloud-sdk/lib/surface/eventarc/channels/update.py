# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
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
"""Command to update the specified channel."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.eventarc import channels
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.eventarc import flags
from googlecloudsdk.command_lib.util.args import labels_util
from googlecloudsdk.core import log

_DETAILED_HELP = {
    'DESCRIPTION':
        '{description}',
    'EXAMPLES':
        """ \
        To update the channel `my-channel` in location `us-central1`, run:

          $ {command} my-channel --location=us-central1

        To configure the channel `my-channel` in location `us-central1` with a Cloud KMS CryptoKey, run:

          $ {command} my-channel --location=us-central1 --crypto-key=projects/PROJECT_ID/locations/KMS_LOCATION/keyRings/KEYRING/cryptoKeys/KEY

        """,
}


@base.ReleaseTracks(base.ReleaseTrack.GA)
@base.DefaultUniverseOnly
class Update(base.UpdateCommand):
  """Update an Eventarc channel."""

  detailed_help = _DETAILED_HELP

  @classmethod
  def Args(cls, parser):
    flags.AddChannelResourceArg(parser, 'Channel to update.', required=True)
    flags.AddCryptoKeyArg(parser, with_clear=True)
    labels_util.AddUpdateLabelsFlags(parser)
    base.ASYNC_FLAG.AddToParser(parser)

  def Run(self, args):
    """Run the update command."""
    client = channels.ChannelClientV1()
    channel_ref = args.CONCEPTS.channel.Parse()

    project_name = channel_ref.Parent().Parent().Name()
    location_name = channel_ref.Parent().Name()
    log.debug('Updating channel {} for project {} in location {}'.format(
        channel_ref.Name(), project_name, location_name))

    original_channel = client.Get(channel_ref)
    labels_update_result = labels_util.Diff.FromUpdateArgs(args).Apply(
        client.LabelsValueCls(), original_channel.labels
    )

    update_mask = client.BuildUpdateMask(
        crypto_key=args.IsSpecified('crypto_key'),
        clear_crypto_key=args.clear_crypto_key,
        labels=labels_update_result.needs_update,
    )

    crypto_key_name = ''
    if args.IsSpecified('crypto_key'):
      crypto_key_name = args.crypto_key

    operation = client.Patch(
        channel_ref,
        client.BuildChannel(
            channel_ref, None, crypto_key_name, labels_update_result.GetOrNone()
        ),
        update_mask,
    )

    if args.async_:
      return operation
    return client.WaitFor(operation, 'Updating', channel_ref)
