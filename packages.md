What about the implications of holding onto packages indefinitely? What happens if a dependency is abandoned? Or the license changes? Or is taken over by bad actors and used as an attack vector? Also, how do we do remove packages safely?

Detecting package usage is harder than it sounds. The name on PyPI doesn't necessarily match what is imported. Also, frameworks like Django and Sphinx have plugin systems that don't necessarily require easily searched direct imports. And then there are automatic imports, like PyFilesystem2's automatic detection of the fs-s3fs and fs.sshfs packages. And, there are packages that are used as a dependency of a dependency. Finally, just because there are tests for a project doesn't mean those tests will detect all edge cases when a dependency is removed.

As one can imagine, identifying packages for removal and safely doing so can be challenging.

This talk will cover why its important to check packages for removal or replacement, lowering the dependency footprint to decrease the risk of compromised packages, unexpected license changes, and other potential threats to projects. It will also cover open source tools to document dependencies and stay on top of changes, so project maintainers can be more aware of what's going on with their dependencies.
