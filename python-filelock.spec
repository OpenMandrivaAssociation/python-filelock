%global pypi_name filelock

Name:           python-%{pypi_name}
Version:        3.7.1
Release:        1
Summary:        A platform independent file lock
Group:          Development/Python
License:        Unlicense
URL:            https://github.com/benediktschmitt/py-filelock
Source0:	https://files.pythonhosted.org/packages/source/f/filelock/filelock-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
%rename python3-%{pypi_name}

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-*.egg-info
