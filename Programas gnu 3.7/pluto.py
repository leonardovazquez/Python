#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: adalm pluto
# Author: Leonardo David Vazquez
# Generated: Mon Dec  6 14:31:58 2021
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import iio
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import pmt
import sip
import sys
from gnuradio import qtgui


class pluto(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "adalm pluto ")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("adalm pluto ")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "pluto")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate_0 = samp_rate_0 = 2804000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate_0, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate_0, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0_1_1_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"entrada", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_1_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_1_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_1_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1_1_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_1_1_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_1_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_1_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_1_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_1_0_0_win)
        self.qtgui_const_sink_x_0_1_1_0 = qtgui.const_sink_c(
        	1024, #size
        	"entrada", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_1_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1_1_0.enable_grid(False)
        self.qtgui_const_sink_x_0_1_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_1_0_win)
        self.pluto_source_0 = iio.pluto_source('usb:1.8.5', 2400000000, 2084000, 20000000, 0x8000, True, True, True, "manual", 10, '', True)
        self.pluto_sink_0 = iio.pluto_sink("'usb:1.8.5", 2400000000, 2084000, 20000000, 0x8000, False, 1, '', True)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=2,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate_0,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((100, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'C:\\Users\\leiit\\Desktop\\pin.jpg', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\leiit\\Desktop\\pin - copia.jpg', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=1,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='11011010110111011000110011110101100010010011110111',
        		pad_for_usrp=False,
        	),
        	payload_length=4,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='11011010110111011000110011110101100010010011110111',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.digital_gmsk_demod_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_const_sink_x_0_1_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.pluto_sink_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.qtgui_const_sink_x_0_1_1_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.pluto_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pluto")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate_0)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate_0)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate_0)


def main(top_block_cls=pluto, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
