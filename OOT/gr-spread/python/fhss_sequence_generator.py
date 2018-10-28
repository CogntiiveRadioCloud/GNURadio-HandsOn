#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import pmt, random
from gnuradio import gr

class fhss_sequence_generator(gr.sync_block):
    """
    docstring for block fhss_sequence_generator
    """
    def __init__(self, seed=0, chan_spacing=1, nchans=8):
        gr.sync_block.__init__(self,
                               name="fhss_sequence_generator",
                               in_sig=None,
                               out_sig=None)

        self.message_port_register_out(pmt.intern("seq"))
        self.message_port_register_in(pmt.intern("trig"))

        self.set_msg_handler(pmt.intern("trig"), self.send_seq)

        random.seed(seed)

        self.chan_spacing = chan_spacing
        self.nchans = nchans

    def send_seq(self, msg):
        x = self.chan_spacing * random.randint(-self.nchans/2, self.nchans/2 - 1)
        self.message_port_pub(pmt.intern("seq"), pmt.from_double(x))
