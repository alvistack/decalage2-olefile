# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-olefile
Epoch: 100
Version: 0.46
Release: 1%{?dist}
BuildArch: noarch
Summary: Python package to parse, read and write Microsoft OLE2 files
License: BSD-3-Clause
URL: https://github.com/decalage2/olefile/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
olefile is a Python package to parse, read and write Microsoft OLE2
files (also called Structured Storage, Compound File Binary Format or
Compound Document File Format), such as Microsoft Office 97-2003
documents, vbaProject.bin in MS Office 2007+ files, Image Composer and
FlashPix files, Outlook messages, StickyNotes, several Microscopy file
formats, McAfee antivirus quarantine files, etc.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-olefile
Summary: Python package to parse, read and write Microsoft OLE2 files
Requires: python3
Provides: python3-olefile = %{epoch}:%{version}-%{release}
Provides: python3dist(olefile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-olefile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(olefile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-olefile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(olefile) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-olefile
olefile is a Python package to parse, read and write Microsoft OLE2
files (also called Structured Storage, Compound File Binary Format or
Compound Document File Format), such as Microsoft Office 97-2003
documents, vbaProject.bin in MS Office 2007+ files, Image Composer and
FlashPix files, Outlook messages, StickyNotes, several Microscopy file
formats, McAfee antivirus quarantine files, etc.

%files -n python%{python3_version_nodots}-olefile
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-olefile
Summary: Python package to parse, read and write Microsoft OLE2 files
Requires: python3
Provides: python3-olefile = %{epoch}:%{version}-%{release}
Provides: python3dist(olefile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-olefile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(olefile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-olefile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(olefile) = %{epoch}:%{version}-%{release}

%description -n python3-olefile
olefile is a Python package to parse, read and write Microsoft OLE2
files (also called Structured Storage, Compound File Binary Format or
Compound Document File Format), such as Microsoft Office 97-2003
documents, vbaProject.bin in MS Office 2007+ files, Image Composer and
FlashPix files, Outlook messages, StickyNotes, several Microscopy file
formats, McAfee antivirus quarantine files, etc.

%files -n python3-olefile
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
