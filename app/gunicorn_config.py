#  Copyright (C) 2020 University of Konstanz -  Data Analysis and Visualization Group
#  This file is part of SciBib <https://github.com/dbvis-ukon/SciBib>.
#
#  SciBib is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SciBib is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SciBib.  If not, see <http://www.gnu.org/licenses/>.

import os

pidfile = "scibib.pid"
worker_tmp_dir = "/dev/shm"
worker_class = "gthread"
workers = 2
worker_connections = 1000
timeout = 30
keepalive = 2
threads = 4
proc_name = "scibib"
bind = "{0}:8080".format(os.getenv('SCIBIB_BIND_ADDRESS', '0.0.0.0'))
backlog = 2048
accesslog = "-"
errorlog = "-"
user = "www-data"
group = "www-data"
