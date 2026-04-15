%define module filelock

Name:		python-filelock
Version:	3.28.0
Release:	1
Summary:	A platform independent file lock
Group:		Development/Python
License:	MIT
URL:		https://github.com/tox-dev/filelock/
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(tomli)
BuildRequires:	python%{pyver}dist(wheel)
%rename	python3-%{module}

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%license LICENSE
%doc README.md
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
